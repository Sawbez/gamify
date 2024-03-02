# React Components

To modify the react components, go to `templates/static/src` where you can change the App.js file or the components folder. After that bundle the site using webpack so that it can be found in the `templates/public` folder. If you don't know how to use webpack go to the public folder and you can find a quick list of instructions there.

# Flask applications

If you want to modify the backend you will need to know flask, luckly with this structure you can pretend that the bundled file is just normal html. To maintain the project stucture, work only in the `templates/apps` folder.

# Running

## Dev

Run both of these at the same time in different terminals:

in "/templates/static"
`npm run watch`

in "/"
`py run.py`

## Prod

Run the first, then the second:

in "/templates/static"
`npm run build`

in "/"
`py run.py prod`