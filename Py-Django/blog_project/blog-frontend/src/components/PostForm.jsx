import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function PostForm(){
  const { id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState({ title:'', content:'', author:'' });

  useEffect(() => {
    if(id){
      api.get(`posts/${id}/`).then(res => setForm(res.data)).catch(err => console.error(err));
    }
  }, [id]);

  const handleChange = (e) => setForm({...form, [e.target.name]: e.target.value});

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      if(id) await api.put(`posts/${id}/`, form);
      else await api.post('posts/', form);
      navigate('/');
    }catch(err){
      console.error(err);
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{display:'flex', flexDirection:'column', gap:8, maxWidth:600}}>
      <input name="title" placeholder="Title" value={form.title} onChange={handleChange} required />
      <textarea name="content" placeholder="Content" value={form.content} onChange={handleChange} rows={8} required />
      <input name="author" placeholder="Author" value={form.author} onChange={handleChange} />
      <div>
        <button type="submit">Save</button>
      </div>
    </form>
  )
}
