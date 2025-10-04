import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Link } from 'react-router-dom';

export default function PostList(){
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try{
      const res = await api.get('posts/');
      setPosts(res.data);
    }catch(err){
      console.error(err);
    }
  }

  const handleDelete = async (id) => {
    if(!window.confirm('Delete post?')) return;
    try{
      await api.delete(`posts/${id}/`);
      fetchPosts();
    }catch(err){
      console.error(err);
    }
  }
    return (
    <div>
      <h2>All posts</h2>
      <ul>
        {posts.map(p => (
          <li key={p.id} style={{marginBottom:12}}>
            <Link to={`/posts/${p.id}`}>{p.title}</Link>
            {' '}
            <button onClick={() => handleDelete(p.id)} style={{marginLeft:8}}>Delete</button>
            {' '}
            <Link to={`/edit/${p.id}`} style={{marginLeft:8}}>Edit</Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
