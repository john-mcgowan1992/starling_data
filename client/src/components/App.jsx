import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { greenA400, greenA200, pink300 } from 'material-ui/styles/colors';

import NavBar from './NavBar.jsx';
import Dashboard from './Dashboard.jsx';

const muiTheme = getMuiTheme({
    palette: {
        primary1Color: greenA200,
        primary2Color: greenA400,
        accent1Color: pink300
    }
})

class App extends Component {
    render() {
        return (
            <MuiThemeProvider muiTheme={muiTheme}>
                <div className="App">
                    <NavBar />
                    <Dashboard />
                </div>
            </MuiThemeProvider>
        )
    }
}

export default App;