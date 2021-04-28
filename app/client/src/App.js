import React from 'react';
import ListItem from './ListItem';

export default class App extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <h1>Kanto Pokedex</h1>
                <input id="search"></input>
                <button>Search</button>

                <ListItem name="Bulbasaur" number="#001" imageURL="http://localhost:3000/pokeImg/#001_Bulbasaur.png"/>
            </div>
        );
    }
}