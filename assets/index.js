
import React from 'react';
import ReactDOM from "react-dom";
import { App } from './src/app';
import { Provider } from 'react-redux';
import {createStore, applyMiddleware, compose} from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './src/redux/root-reducer';

/*ReactDOM.render(
  <h1>Hello, react!</h1>,
  document.getElementById('root')
);*/
const middleware = [thunk]
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSIONS_COMPOSE__ || compose
const store = createStore(rootReducer, composeEnhancers(applyMiddleware(...middleware)))

ReactDOM.render(<App />, document.getElementById('root'));




/*import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
//import * as serviceWorker from './serviceWorker';
//import { Link } from 'react-router-dom';

ReactDOM.render(<App />, document.getElementById('root'));*/

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();
