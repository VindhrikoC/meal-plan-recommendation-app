import React from 'react';
import './App.css';
import IngredientList from './components/Ingredients';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Meal Plan Recommendation App</h1>
      </header>
      <main>
        <IngredientList />
      </main>
    </div>
  );
};

export default App;
