import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import Avatar from 'material-ui/Avatar';

class NavBar extends Component {
    constructor() {
        super()
        this.styleStarling = {
            borderRadius: "none",
            backgroundColor: "none",
            width: "35px",
            height: "35px",
            margin: "5px 10px"
        }
    }
    render() {
        return (
            <AppBar iconElementLeft={<div />} iconElementRight={<Avatar src="/api/public/starling.png" style={this.styleStarling} />} title="Starling Analytics"/>
        )
    }
}

export default NavBar;