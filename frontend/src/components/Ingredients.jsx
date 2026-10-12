import React, { useEffect, useState } from 'react';
import AddIngredientForm from './AddIngredientForm';
import api from '../api';

const IngredientList = () => {
  const [ingredients, setIngredients] = useState([]);

  const fetchIngredients = async () => {
    try {
      const response = await api.get('/ingredients');
      setIngredients(response.data.ingredients);
    } catch (error) {
      console.error("Error fetching ingredients", error);
    }
  };

  const addIngredient = async (ingredientName) => {
    try {
      await api.post('/ingredients', { name: ingredientName });
      fetchIngredients();  // Refresh the list after adding an ingredient
    } catch (error) {
      console.error("Error adding ingredient", error);
    }
  };

  useEffect(() => {
    fetchIngredients();
  }, []);

  return (
    <div>
      <h2>Ingredient List</h2>
      <ul>
        {ingredients.map((ingredient, index) => (
          <li key={index}>{ingredient.name}</li>
        ))}
      </ul>
      <AddIngredientForm addIngredient={addIngredient} />
    </div>
  );
};

export default IngredientList;