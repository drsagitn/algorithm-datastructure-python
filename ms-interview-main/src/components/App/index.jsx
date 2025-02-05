// src/App.js
import React from 'react';
import { themes } from '../Data';
import QuestionList from '../QuestionList';

const App = () => {
  return (
    <div className="App">
      {/* <h1>Microsoft Interview</h1> */}
      <div className="layout bg-gray-700">
        <QuestionList themes={themes} />
      </div>
    </div>
  );
};

export default App;
