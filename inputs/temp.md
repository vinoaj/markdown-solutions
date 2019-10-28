There may be occasions where you need to retrieve or modify Google Tag Manager data layer values on the client using JavaScript. 

Trying to directly access the values through the `dataLayer` object is not straightforward. If you inspect a `dataLayer` object on a page, you will see that it looks something like:



The dataLayer object is a collection of dataLayer states at each event recorded by Google Tag Manager. Therefore in order to find the current state of a dataLayer variable, you will need to access the `dataLayer` object, find the last recorded state, and retrieve the value from there.

Thankfully the Google Tag Manager JavaScript API provides convenience functions to access and manipulate the values of data layer variables.

**Get the value of a variable**
`window['google_tag_manager']['GTM-XXXXXXX'].dataLayer.get('nameOfVariable');`

**Set the value of a variable**
`window['google_tag_manager']['GTM-XXXXXXX'].dataLayer.set('nameOfVariable', 'newValue');`

**Reset a variable**
`window['google_tag_manager']['GTM-XXXXXXX'].dataLayer.reset('nameOfVariable');`