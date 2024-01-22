import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from './Api';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginResult, setLoginResult] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await api.post('/login', { username, password });
      console.log('Login successful:', response.data);

      setLoginResult('hi'+response.data+'. you have successfully logged in.');
     
      if (response.data) {
        const name  = response.data;
        navigate('/app/'+name);
      }
    } catch (error) {
      console.error('Login error:', error.response.data.detail);
      setLoginResult(error.response.data.detail);
    }
  };

  // If login is successful, render null (or you can replace it with another component)
  if (loginResult) {
    return null;
  }

  return (
    <div className="container mt-4">
      <label htmlFor="username" className="form-label">Username:</label>
      <input type="text" id="username" className="form-control" value={username} onChange={(e) => setUsername(e.target.value)} />
      <label htmlFor="password" className="form-label mt-3">Password:</label>
      <input type="password" id="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin} className="btn btn-primary mt-3">Login</button>

      {/* Display login result if present */}
      {loginResult && (
        <div className="alert alert-info mt-3" role="alert">
          {loginResult}
        </div>
      )}
    </div>
  );
};

export default LoginForm;
