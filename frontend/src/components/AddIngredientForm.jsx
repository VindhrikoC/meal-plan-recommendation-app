import React, { useState } from 'react';

const AddIngredientForm = ({ addIngredient, addUser, activeUser, error }) => {
  const [ingredientName, setIngredientName] = useState('');
  const [userName, setUserName] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const name = ingredientName.trim();
    if (name && await addIngredient(name)) {
      setIngredientName('');
    }
  };

  const handleUserSubmit = async (event) => {
    event.preventDefault();
    const name = userName.trim();
    if (name && await addUser(name)) {
      setUserName('');
    }
  };

  return (
    <>
      <form onSubmit={handleUserSubmit}>
        <input
          type="text"
          value={userName}
          onChange={(e) => setUserName(e.target.value)}
          placeholder="Enter username"
          aria-label="Username"
        />
        <button type="submit">Load or Create User</button>
      </form>
      {error && <p role="alert">{error}</p>}
      {activeUser && (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={ingredientName}
            onChange={(e) => setIngredientName(e.target.value)}
            placeholder="Enter Ingredient name"
            aria-label="Ingredient name"
          />
          <button type="submit">Add Ingredient</button>
        </form>
      )}
    </>
  );
};

export default AddIngredientForm;