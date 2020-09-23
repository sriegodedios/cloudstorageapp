import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Switch } from "react-router";
import 'foundation-sites/dist/css/foundation.min.css';

// import components
import { Button, Colors } from 'react-foundation';

// Use components ...
function SubmitButton() {
  return <Button color={Colors.SUCCESS}>Submit</Button>;
}


export class App extends React.Component{
    render(){
        return(
           <SubmitButton></SubmitButton>
        )}
}


