if (document.body.id === "encrypter-page") {
    console.log("Running encrypter code");
    const encryptBtn = document.getElementById('encryptBtn');
    encryptBtn.addEventListener("click", async () => {
    const rawtext = document.getElementById('rawtext').value;
    const a = document.getElementById('coeffA').value;
    const b = document.getElementById('coeffB').value;
    const c = document.getElementById('coeffC').value;
    const encryptedascii = await window.pywebview.api.encrypt_text(rawtext, a, b, c);
    document.getElementById("encryptedascii").innerText = encryptedascii;
    console.log(encryptedascii);
});
}
if (document.body.id === "decrypter-page") {
    console.log("Running decrypter code");
    const decryptBtn = document.getElementById('decryptBtn');
    decryptBtn.addEventListener("click", async () => {
    const unprocessed_text_list = document.getElementById('unprocessed_text_list').value;
    const a = document.getElementById('coeffA').value;
    const b = document.getElementById('coeffB').value;
    const c = document.getElementById('coeffC').value;
    const finaltext = await window.pywebview.api.decrypt_text(unprocessed_text_list, a, b, c);
    console.log(finaltext)
})
}























































if (document.body.id === "page2") {
    console.log("Running Page 2 code...");
    // put code for page2 here
}