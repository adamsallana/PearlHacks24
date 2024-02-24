// id variables for each link
const searchLink = document.getElementById("search-link");
const searchLinkResult = document.getElementById("search-link-res");
const uploadNotes = document.getElementById("upload-notes");
const uploadNotesConf = document.getElementById("upload-note-conf");

// connecting mouse click to each function
searchLink.addEventListener("click", () => {
    visitSearch();
})

searchLinkResult.addEventListener("click", () => {
    visitSearchResult();
})

uploadNotes.addEventListener("click", () => {
    visitUploadNotes();
})

uploadNotesConf.addEventListener("click", () => {
    visitUploadNotesConf();
})


//functions for each site
function visitSearch() {
    window.location="./searchnotes.html"
}

function visitSearchResult() {
    window.location="./searchnotes-res.html"
}

function visitUploadNotes() {
    window.location="./uploadnotes.html"
}

function visitUploadNotesConf() {
    window.location="./uploadnotes-conf.html"
}