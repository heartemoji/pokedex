import React from 'react';

export default class ListItem extends React.Component {
    
    render() {
        return (
            <div class="listItem">
                <img class="listItemImg" src={this.props.imageURL} height="50px" width="50px" alt={this.props.name}/>
                <h3>{this.props.number} - {this.props.name}</h3>
                <h4>{this.props.type}</h4>
            </div>
        );
    }
}