This guide will walk you through combining data between two sheets in a Google Sheets spreadsheet. It makes use of a formula that utilises the [`MATCH()`](https://support.google.com/docs/answer/3093378?hl=en&ref_topic=3105472), [`VLOOKUP()`](https://support.google.com/docs/answer/3093318?hl=en&ref_topic=3105472), and [`ARRAYFORMULA`](https://support.google.com/docs/answer/3093275?hl=en) functions.

#TL;DR
Use this formula:
```
=ARRAYFORMULA(
    VLOOKUP($A$2:$A, Sheet2!$A:$D,
        MATCH(M$1, Sheet2!$1:$1, 0), TRUE
    )
)
```


#Scenario
You have been asked to compare the sales performance of your products against daily price changes across your competitors.

You receive multiple spreadsheets with data relevant to your analysis. Some of these data sources need to be combined. You could upload the sheets into a database, with each sheet represented as a separate table, and then use SQL to join tables. However, this solution takes time to set up and would be overkill if we don't use it on a regular basis. 

Instead, by chaining a few functions together in a formula, we can quickly combine the data in Google Sheets itself.

##The Data
You have two spreadsheets with data that is relevant for your analysis.

**Spreadsheet 1 (Pricing Data)** contains daily pricing information for your and your competitors' products.
[TODO: image]

**Spreadsheet 2 (Sales Data)** contains daily sales performance data.
[TODO: image]

You need to combine data from both sources in order to determine:
+ the relationship between Competitor Z's pricing and how many units you sold
+ whether deviating greatly from the average price impacts how many units you sell

Let's now look at how we combine these different datasets in Google Sheets.

#Prepare the data
##Key verification
Looking at the two datasets, it becomes clear that the key we will join the data on is the *Date* column. At this point you will want to do a sanity check on the keys:

+ Are they formatted correctly (date format) and consistently?
+ Are there any missing keys in either dataset?
+ Are there any duplicates within a single dataset?
+ Are there any invalid values?
+ ... and so on ...

##Place the data in individual sheets within a single Google Sheets spreadsheet

+ [Create a new Google Sheets spreadsheet](https://support.google.com/docs/topic/20329?hl=en&ref_topic=1361470)
+ Copy the data from *Spreadsheet 1* and paste it into the sheet (*Sheet 1*)
+ Add a new sheet
+ Copy the data from *Spreadsheet 2* and paste it into the new sheet (*Sheet 2*)
+ Go back to *Sheet 1* and create new column headings for the fields you want from *Sheet 2*. The column names **must match** across sheets.
  + In this example we want *Units Sold* and *% Sold*

At this stage *Sheet 1* looks something like
[TODO: image]


#Combining the data
In cell *H2* insert the following formula:
```
=ARRAYFORMULA(
    VLOOKUP($A$2:$A, Sheet2!$A:$D,
        MATCH(H$1, Sheet2!$1:$1, 0), TRUE
    )
)
```

Now copy *H2* and paste it into *I2*

And voila! We now have the relevant sales performance data combined with our pricing intelligence data.
[TODO: image]


#The formula explained
Let's break down the formula so we can better understand what it does.

##MATCH()
The `MATCH()` function returns the position of a search term in a given column or row. In this case, we are asking it to tell us which column in *Sheet 2* holds the data we are interested in.

MATCH(H$1, Sheet2!$1:$1, 0)

Let's break this down further:

+ **Search term**: `H$1` references the first cell of column H -> "Units Sold". 
+ **Search range**: `Sheet2!$1:$1` references the entire first row of *Sheet 2* -> row of column names
+ **Search type**: `0` for exact match since our range is not sorted

So in human speak, we are asking "Where in the first row of Sheet 2 does 'Units Sold' appear?"

The answer should be `2` - i.e. the second cell of the row of column names

##VLOOKUP()
The `VLOOKUP()` function is commonly used to search a range for a value in the first column and then return a corresponding value from another column. 

If we used `VLOOKUP()` on its own (i.e. without combining it with `MATCH()` and `ARRAYFORMULA()`) this is how the function would be used to return the value held in the 2nd column of *Sheet 2*

VLOOKUP(A2, Sheet2!$A:$D, 2, FALSE)

Let's break this down further:

+ **Search term**: `A2` references the date in that cell -> "1/1/2018"
+ **Data range**: `Sheet2!$A:$D` references columns *A-D* in *Sheet 2*
+ **Column index**: `2` indicates we are interested in the data held in the 2nd column
+ **Search column sorted**: `TRUE` to indicate that the search column (i.e. the first column in the data range) is sorted. Use `FALSE` if the search column is not sorted.

This should return the value `44` - i.e. the value in the 2nd column of *Sheet 2* in the row where the value of the first cell is *1/1/2018*

Now there are two issues with this formula:
1. The column index is hardcoded. This means that if the columns get re-ordered in *Sheet 2* in the future, we will need to go back and edit all our formulae to reference the new column number.
1. This formula will need to be pasted into every relevant cell in the sheet. This means if we need to modify the formula in future, we will need to ensure every cell has been edited. The risk is we might miss some cells.

The first issue is solved by using the above `MATCH()` formula in place of the hard-coded column index value. It will always give us the current column index for the given column name.

VLOOKUP(A2, Sheet2!$A:$D, MATCH(H$1, Sheet2!$1:$1, FALSE)

To solve the second issue we need to use `ARRAYFORMULA()`

##ARRAYFORMULA()
One way `ARRAYFORMULA()` is used is to convert non-array functions into array-like functions. 

What does this mean? In the above `VLOOKUP()` function call, we can only reference a single cell for the search term. It would be more convenient if we could pass it a reference to a column (i.e. an array of size `1 x total_num_rows`) and ask it to iterate through each value and perform a corresponding `VLOOKUP`. Additionally, the found values should be stored in an array and be output across the corresponding number of rows and columns. This is where `ARRAYFORMULA()` plays a role:

```
=ARRAYFORMULA(
    VLOOKUP($A$2:$A, Sheet2!$A:$D,
        MATCH(H$1, Sheet2!$1:$1, 0), TRUE
    )
)
```

Simply put, the above `ARRAYFORMULA()` function call references the above `VLOOKUP` function call with one key difference: `A2` (reference to a single cell) has been replaced with `$A$2:$A` (reference to column 1's contents starting from the 2nd row).




#Resources
+ [Google Sheets VLOOKUP documentation](https://support.google.com/docs/answer/3093318?hl=en&ref_topic=3105472)
+ [Google Sheets MATCH documentation](https://support.google.com/docs/answer/3093378?hl=en&ref_topic=3105472)
+ [Google Sheets ARRAYFORMULA documentation](https://support.google.com/docs/answer/3093275?hl=en)