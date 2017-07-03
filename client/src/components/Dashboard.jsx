import React, { Component } from 'react';
import { Card, CardActions, CardHeader, CardMedia} from 'material-ui/Card';
import { List, ListItem } from 'material-ui/List';
import Avatar from 'material-ui/Avatar';
// import { Bar } from 'react-chartjs';
import { VictoryBar, VictoryChart, VictoryAxis, VictoryTooltip,VictoryTheme } from 'victory';

import Timeline from 'material-ui/svg-icons/action/timeline';
import AttachMoney from 'material-ui/svg-icons/editor/attach-money';
import Group from 'material-ui/svg-icons/social/group';
import Poll from 'material-ui/svg-icons/social/poll';

import './Dashboard.css';

const innerStyle = {
    margin: "auto",
    textAlign: "center"
}

const vData = [
  {department: "Engineering", earnings: 0},
  {department: "Sales", earnings: 0},
  {department: "Support", earnings: 0}
];

const chartData = [ [3], [17], [12] ];

class Dashboard extends Component {
    constructor() {
        super()
        this.state = {
            averages: vData,
            headCount: [],
            total: {"total": 0}
        }
        this.styleEmployees = {
            maxWidth: "85%",
            margin: "0 auto 2%",
            minHeight: "300px"
        }
        this.styleCompensation = {
            maxWidth: "85%",
            margin: "0 auto 2%",
            minHeight: "450px"
        }
        this.avatarStyle = {
            borderRadius: "none",
            backgroundColor: "none",
            width: "30px", 
            height: "30px"
        }
    }
    componentDidMount() {
        fetch('/api/averages')
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            var newData = Object.assign({}, vData)
            console.log('new data: ', data)
            newData[0].earnings = data['Engineering'];
            newData[1].earnings = data['Sales'];
            newData[2].earnings = data['Support'];
            // this.setState({"averages": newData})
        })
        fetch("/api/headcount_over_time/engineering")
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            console.log("headcount: ", data)
            this.setState({headCount: data})
        })
        fetch("/api/headcount_total")
        .then(res => {
            return res.json()
        })
        .then(count => {
            this.setState({"total": count})
            console.log('state: ', this.state)
        })
        // fetch("/api/highest_earners")
        // .then(res => {
        //     return res.json()
        // })
        // .then(data => {
        //     this.setState({"earners": data})
        //     console.log('earn:', data);
        // })
    }
    render() {
        return (
            <div className="Dashboard">
                <div className="BumperLeft">
                    <Card>
                        <CardHeader avatar={<Avatar style={this.avatarStyle} src="/api/public/starling.png"/> } title="Starling" subtitle="People Analytics" />
                        <CardMedia>
                            <List>
                                <ListItem primaryText={ this.state.total.total + " Employees" }leftIcon={<Group />} disabled={true} />
                                <ListItem primaryText="21% annual growth" leftIcon={<Timeline />} disabled={true} />
                                <ListItem primaryText="7% Attrition" leftIcon={<Poll />} disabled={true} />
                            </List>
                        </CardMedia>
                    </Card>
                </div>
                <div className="mainContainer">
                    <Card style={ this.styleCompensation }>
                        <CardHeader avatar={<AttachMoney />} title="Compensation" subtitle="By department" />
                        <CardMedia>
                            <VictoryChart domainPadding={20} theme={VictoryTheme.material}>
                                <VictoryAxis tickValues={ [1, 2, 3] } tickFormat={ ["Engineering", "Sales", "Support"] } />
                                <VictoryAxis dependentAxis tickFormat={ (x) => (`$${x / 1000}k`) } />
                                <VictoryBar data={ this.state.averages } x="department" y="earnings" labelComponent={<VictoryTooltip />} />
                            </VictoryChart>
                        </CardMedia>
                    </Card>
                    <Card style={ this.styleEmployees }>
                        <CardHeader avatar={<Timeline />} title="Company Growth" subtitle="Number of Employees" />
                    </Card>
                </div>
                <div className="BumperRight">
                    <Card>
                        <CardHeader title="Top Earners" subtitle="Company-wide" />
                    </Card>
                </div>
            </div>
        )
    }
}

export default Dashboard;