import React, { Component, Fragment } from "react";
import MainLayout from "../../Layout/MainLayout";
import { Link } from "react-router-dom";
import { get_posted_food } from "../../../actions/food";
import { Row, Col, Select, Button, Transfer } from "antd";
import { connect } from "react-redux";

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  componentDidMount() { }

  render() {
   
    return (
      <MainLayout>
        <Fragment>
         
          <h1>List of Posted Food</h1>
          <br />
          
         
          {/* <p style={{textAlign:"center",fontSize:'66px'}}>WELCOME...</p> */}
        </Fragment>
        
        
      </MainLayout>
    );
  }
}

const mapStateToProps = (state) => ({
  // user: state.auth.user,
  all_posted_food: state.food.all_posted_food
});

export default connect(mapStateToProps, {
  get_posted_food,
})(Dashboard);
