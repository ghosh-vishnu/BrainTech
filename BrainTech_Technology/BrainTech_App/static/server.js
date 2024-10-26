const express = require('express');
const mysql = require('mysql2');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();


// Set up MySQL connection
const db = mysql.createConnection({
    host: "127.0.0.1",
    user: "root", // replace with your MySQL username
    password: "", // replace with your MySQL password
    database: "braintech_technology",
    port : 3307
});

db.connect(err => {
    if (err) {
        console.error('Error connecting to the database:', err);
        return;
    }
    console.log('Connected to the MySQL database.');
});

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// Route to handle certificate check
app.get('/checkCertificate', (req, res) => {
    const certificateId = req.query.id;

    if (!certificateId) {
        return res.json({ success: false, message: 'Certificate ID is required.' });
    }

    const query = 'SELECT * FROM certificates WHERE Id = ?';
    db.query(query, [certificateId], (err, results) => {
        if (err) {
            console.error('Error querying the database:', err);
            return res.json({ success: false, message: 'Database query error.' });
        }

        if (results.length > 0) {
            res.json({ success: true, data: results[0] });
        } else {
            res.json({ success: false, message: 'Certificate not found or unauthorized.' });
        }
    });
});

// Route to handle certificate insertion
app.post('/addCertificate', (req, res) => {
    const { name, type, issued } = req.body;

    if (!name || !type || !issued) {
        return res.json({ success: false, message: 'All fields are required.' });
    }

    const query = 'INSERT INTO certificates (Name, Type, Issued) VALUES (?, ?, ?)';
    db.query(query, [name, type, issued], (err, result) => {
        if (err) {
            console.error('Error inserting into the database:', err);
            return res.json({ success: false, message: 'Database insertion error.' });
        }

        res.json({ success: true, message: 'Certificate added successfully.', data: result });
    });
});

const port= 3000
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
