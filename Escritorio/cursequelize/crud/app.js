const express =require('express');
const app= express();
const sequelize = require('./database/db');
const User = require('./database/models/user')


// settings
const PORT = process.env.PORT || 5000;
// Routes
app.get('/', function (req, res){
    // Crear un usuario

    User.create({
        name: 'Andres',
        birthday: new Date(2002, 07, 17),
    }).then(user => {
        res.json(user);
    });
    // Listar todos los usuarios
    // User.findAll().then(user =>{
    //     res.json(user);
    // })
});
// Run the server
app.listen(PORT, function (){
    console.log(`listening on http://localhost:${PORT}`)
    // Conect to database
    // force: false no reset tables
    sequelize.sync({force: true }).then(() =>{
    console.log('Connection has been established successfully.')
    }).catch(error => {
        console.log('Unable to connect to the database:',error);
    })
});