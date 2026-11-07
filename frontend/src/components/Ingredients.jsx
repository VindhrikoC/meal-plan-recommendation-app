import React, { useState } from 'react';
import AddIngredientForm from './AddIngredientForm';
import api from '../api';

const IngredientList = () => {
  const [activeUser, setActiveUser] = useState(null);
  const [error, setError] = useState('');

  const addUser = async (userName) => {
    try {
      setError('');
      let user;
      try {
        const response = await api.get(
          `/api/users/by-username/${encodeURIComponent(userName)}`
        );
        user = response.data;
      } catch (lookupError) {
        if (lookupError.response?.status !== 404) {
          throw lookupError;
        }
        const response = await api.post('/api/users/', {
          user_name: userName,
          ingredients: [],
        });
        user = response.data;
      }
      setActiveUser(user);
      return true;
    } catch (error) {
      console.error("Error loading or creating user", error);
      setError(error.response?.data?.detail || "Could not load or create user.");
      return false;
    }
  };

  const addIngredient = async (ingredientName) => {
    try {
      setError('');
      const response = await api.put(
        `/api/users/${activeUser.id}/ingredients`,
        [ingredientName]
      );
      setActiveUser(response.data);
      return true;
    } catch (error) {
      console.error("Error adding ingredient", error);
      setError(error.response?.data?.detail || "Could not add ingredient.");
      return false;
    }
  };

  return (
    <div>
      <h2>Find or Create User</h2>
      <AddIngredientForm
        addIngredient={addIngredient}
        addUser={addUser}
        activeUser={activeUser}
        error={error}
      />
      {activeUser && (
        <section>
          <h2>{activeUser.user_name}'s Ingredients</h2>
          {activeUser.ingredients.length > 0 ? (
            <ul>
              {activeUser.ingredients.map((ingredient, index) => (
                <li key={`${ingredient}-${index}`}>{ingredient}</li>
              ))}
            </ul>
          ) : (
            <p>No ingredients saved yet.</p>
          )}
        </section>
      )}
    </div>
  );
};

export default IngredientList;