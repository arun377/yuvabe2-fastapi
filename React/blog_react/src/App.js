import React, { useState, useEffect } from "react";
import api from './Api';
import { useParams } from 'react-router-dom';




const App = () => {
  const [transaction, setTransaction] = useState([]);
  const [get_res, setGet_Res] = useState([]);

  const [blogData, setBlogData] = useState({
    id: '',
    title: '',
    body: '',
    date:''

  });

  const fetchTransactions = async () => {
    const response = await api.get('/blog/');
    setTransaction(response.data);
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  const handleInputChange = (e) => {
    setBlogData((prevData) => ({
      ...prevData,
      [e.target.name]: e.target.value,
    }));
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/blog/', blogData);
    fetchTransactions();
    setBlogData({
      id: '',
      title: '',
      body: '',
      date:''
    });
  };

  const handleFormGet = async (event) => {
    event.preventDefault();
    const res=await api.get('/blog/'+blogData.date);
    console.log(res.data);
    setGet_Res(res.data);
    fetchTransactions();
    setBlogData({
      id: '',
      title: '',
      body: '',
      date:''
    });
  };

  

  const { name } = useParams();

  return (
    <div>
      <nav className="navbar navbar-dark bg-success">
        <div className='container-fluid'>
          <a className="navbar-brand" href='#'>
            blog-site
          </a>
          <p>{name}</p>
        </div>
      </nav>
      <div className="container">
        <form >
          <div className="mb-3 mt-3">
            <label htmlFor='id' className="form-label">
              ID
            </label>
            <input type="text" className='form-control' id='id' name='id' onChange={handleInputChange} value={blogData.id} />
          </div>

          <div className="mb-3">
            <label htmlFor='title' className="form-label">
              Title
            </label>
            <input type="text" className='form-control' id='title' name='title' onChange={handleInputChange} value={blogData.title} />
          </div>

          <div className="mb-3">
            <label htmlFor='body' className="form-label">
              Body
            </label>
            <input type="text" className='form-control' id='body' name='body' onChange={handleInputChange} value={blogData.body} />
          </div>

          <div className="mb-3">
            <label htmlFor='date' className="form-label">
              date
            </label>
            <input type="text" className='form-control' id='date' name='date' placeholder="dd-mm-yyyy" onChange={handleInputChange} value={blogData.date} />
          </div>

          <button type='submit' className=' btn btn-success' onClick={handleFormSubmit}>Submit</button>
          <button type='submit' className='m-5 btn btn-primary' onClick={handleFormGet}>get</button>
        </form>

        <table className='table table-striped table-bordered table-hover'>
<thead>
<tr>
<th>title</th>
<th>content </th>
<th>Date </th>


</tr>
</thead>
<tbody>
{transaction.map((transaction) => (
<tr key={transaction.id}>
<td>{transaction.title}</td>
<td>{transaction.body}</td>
<td>{transaction.date}</td>

</tr>
))}
</tbody>
</table>

<table className='table table-striped table-bordered table-hover'>
        <thead>
          <tr>
            <th>Title</th>
            <th>Content</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {get_res.map((blog) => (
            <tr key={blog.id}>
              <td>{blog.title}</td>
              <td>{blog.body}</td>
              <td>{blog.date}</td>
            </tr>
          ))}
        </tbody>
      </table>

      </div>
    </div>
  );
};

export default App;
