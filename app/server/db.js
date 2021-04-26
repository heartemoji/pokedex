import mongodb from 'mongodb';

const MongoClient = mongodb.MongoClient;
const URL = "mongodb://localhost:27017";

/**
 * Get's all pokemon entries in the database
 */
export default function getAllPokemon() {
    return new Promise((resolve, reject) => {
        MongoClient.connect(URL, (err, mongodb) => {
            if (err) reject(err);

            let PokeDB = mongodb.db('pokedex');
            PokeDB.collection('pokemon').find().toArray((err, result) => {
                if (err) reject(err);
                console.log(result);

                mongodb.close();

                resolve(result)
            });
        });
    });
}
