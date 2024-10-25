import React, { useState } from 'react';
import axios from 'axios';

function Calculator() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/calculate', {
        expression: expression
      });
      setResult(response.data.result);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
      setResult(null);
    }
  };

  return (
    <div>
      <h1>NPI Calculator</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={expression}
          onChange={(e) => setExpression(e.target.value)}
          placeholder="Enter NPI expression"
        />
        <button type="submit">Calculate</button>
      </form>
      {result && <h2>Result: {result}</h2>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default Calculator;
