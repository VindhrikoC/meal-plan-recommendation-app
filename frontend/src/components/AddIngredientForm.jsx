import React, { useState } from 'react';

const AddIngredientForm = ({ addIngredient }) => {
  const [ingredientName, setIngredientName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (ingredientName) {
      addIngredient(ingredientName);
      setIngredientName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={ingredientName}
        onChange={(e) => setIngredientName(e.target.value)}
        placeholder="Enter Ingredient name"
      />
      <button type="submit">Add Ingredient</button>
    </form>
  );
};

export default AddIngredientForm;