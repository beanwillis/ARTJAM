const admin = require("firebase-admin")
const serviceAccount = require("./artjam-287602-c4a440e2da91.json");
const data = require("./skills.json")

const collectionKey = "Skills";

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
})

const firestore = admin.firestore();

if (data && (typeof data === "object")) {
    Object.keys(data).forEach(docKey => {
     firestore.collection(collectionKey).add(data[docKey]).then((res) => {
        console.log("Document " + docKey + " successfully written!");
    }).catch((error) => {
       console.error("Error writing document: ", error);
    });
});
}