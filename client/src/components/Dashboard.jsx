import React, { Component } from 'react';
import { Card, CardActions, CardHeader, CardMedia} from 'material-ui/Card';
import { List, ListItem } from 'material-ui/List';
import Avatar from 'material-ui/Avatar';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import { Table, TableHeader, TableBody, TableHeaderColumn, TableRowColumn, TableRow } from 'material-ui/Table';
import { VictoryBar, VictoryLine, VictoryChart, VictoryAxis, VictoryTooltip,VictoryTheme } from 'victory';

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
            headcountDepartment: {display: "Total"},
            total: {"total": 0},
            earners: []
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
        this.toggleDepartment = (event, index, val) => {
            let newDept = {"display": val};
            this.setState({"headcountDepartment": newDept})
        } 
    }
    componentDidMount() {
        fetch('/api/averages')
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            var newData = Object.assign({}, vData)
            newData[0].earnings = data['Engineering'];
            newData[1].earnings = data['Sales'];
            newData[2].earnings = data['Support'];
            // this.setState({"averages": newData})
        })
        fetch("/api/headcount_over_time")
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            this.setState({headCount: data})
            console.log('stata: ', this.state);
        })
        fetch("/api/headcount_total")
        .then(res => {
            return res.json()
        })
        .then(count => {
            this.setState({"total": count})
        })
        fetch("/api/highest_earners")
        .then(res => {
            return res.json()
        })
        .then(data => {
            let jsonified = data.map(JSON.parse);
            this.setState({"earners": jsonified})
        })
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
                        <CardMedia>
                            <CardActions>
                                <SelectField floatingLabelText="Department" value={this.state.headcountDepartment.display} onChange={this.toggleDepartment} >
                                    <MenuItem value={"Total"} primaryText="All Departments" />
                                    <MenuItem value={"Engineering"} primaryText="Engineering" />
                                    <MenuItem value={"Sales"} primaryText="Sales" />
                                    <MenuItem value={"Support"} primaryText="Support" />
                                </SelectField>
                            </CardActions>
                            <VictoryChart domainPadding={3} theme={VictoryTheme.material}>
                                <VictoryAxis fixLabelOverlap={true} />
                                <VictoryAxis fixLabelOverlap={true} dependentAxis tickFormat={ (x) => { return x } } />
                                <VictoryLine data={this.state.headCount} x="chart_label" y={this.state.headcountDepartment.display} />
                            </VictoryChart>
                        </CardMedia>
                    </Card>
                </div>
                <div className="BumperRight">
                    <Card>
                        <CardHeader title="Top Earners" subtitle="Company-wide" />
                        <CardMedia>
                            <Table>
                                <TableHeader displaySelectAll={false} adjustForCheckbox={false}>
                                    <TableRow>
                                        <TableHeaderColumn>Emp. ID</TableHeaderColumn>
                                        <TableHeaderColumn>Salary</TableHeaderColumn>
                                    </TableRow>
                                </TableHeader>
                                <TableBody displayRowCheckbox={false} >
                                    {
                                        this.state.earners.map((employee, i) => 
                                            <TableRow key={i}>
                                                <TableRowColumn>{employee.id}</TableRowColumn>
                                                <TableRowColumn>$ {employee.salary}</TableRowColumn>
                                            </TableRow>
                                        )
                                    }
                                </TableBody>
                            </Table>
                        </CardMedia>
                    </Card>
                </div>
            </div>
        )
    }
}

export default Dashboard;