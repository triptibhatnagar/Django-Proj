import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../services/api';

export default function PostDetail(){
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    api.get(`posts/${id}/`)
      .then(res => setPost(res.data))
      .catch(err => console.error(err));
  }, [id]);

  if(!post) return <div>Loading...</div>;

  return (
    <div>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
      <p><em>Author: {post.author}</em></p>
      <Link to="/">Back</Link>
    </div>
  )
}
