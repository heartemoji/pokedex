/**
 *      app.js
 *      @author Tom Amaral <thomasamaral2016@gmail.com>
 *      @description Entry point for the backend of the Pokedex web application
 */
import express from 'express';
import path from 'path';
import getAllPokemon from './db';

const app = express()
const port = 3000


app.use(express.static(path.join(__dirname, '../client', 'build')));


/**
 * Index route
 */
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../client', 'build', 'index.html'));
});

//#region API endpoints
app.get('/api/getAllPokemon', (req, res) => {
    console.log(req.body)
    //TODO sanitize input
    getAllPokemon().then((result) => {

        res.send(result);
    }, (err) => {
        console.error(err);
    })
    
});


app.listen(port, () => {
    console.log(`Listening on port ${port}`);
})