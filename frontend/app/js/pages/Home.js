import React, { Component } from 'react';

class Home extends Component {

  render() {
    return (
      <div className={this.props.className}>
        <h2>DJ05 Example</h2>

        <div className="row">
          <div className="col-md-4">
            Uses React for presentation
          </div>
          <div className="col-md-4">
            Uses Redux for data management
          </div>
          <div className="col-md-4">
            Uses Django backend
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
