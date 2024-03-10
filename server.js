const express = require("express");
const multer = require('multer');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors()); // Allows incoming requests from any IP

// Start by creating some disk storage options:
const storage = multer.diskStorage({
    destination: function (req, file, callback) {
        callback(null, 'C:/Users/balag/OneDrive/Documents/studentpdf');
    },
    filename: function (req, file, callback) {
        callback(null, file.originalname);
    }
});

// Set saved storage options:
const upload = multer({ storage: storage });

app.post("/api", upload.array("files"), (req, res) => {
    console.log(req.body);
    console.log(req.files);
    res.json({ message: "File(s) uploaded successfully" });
});

// Handle GET request for root URL
app.get("/", (req, res) => {
    res.send("Hello World!");
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
