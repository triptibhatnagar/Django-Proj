import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import PostList from './components/PostList';
import PostDetail from './components/PostDetail';
import PostForm from './components/PostForm';

export default function App(){
  return (
    <BrowserRouter>
      <div style={{padding:20}}>
        <header>
          <h1>My Blog</h1>
          <nav>
            <Link to="/">Home</Link> | <Link to="/create">Create</Link>
          </nav>
        </header>

        <main style={{marginTop:20}}>
          <Routes>
            <Route path="/" element={<PostList/>} />
            <Route path="/posts/:id" element={<PostDetail/>} />
            <Route path="/create" element={<PostForm/>} />
            <Route path="/edit/:id" element={<PostForm/>} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}