import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './App.css'
import './Dashboard'
import Dashboard from './Dashboard'

function App() {

  return (
    <>
      <div className="house">
        🏠
      </div>
      <h1>Sussex Mews To Do List</h1>
      <div className="card">
       
        <button onClick={() => createRoot(document.getElementById('root')!).render(
          <StrictMode>
            <Dashboard />
          </StrictMode>,
        )}>
          Dashboard
        </button>
        <button onClick={() => createRoot(document.getElementById('root')!).render(
          <StrictMode>
            <Dashboard />
          </StrictMode>,
        )}>
          Add Tasks
        </button>
      </div>
    </>
  )
}

export default App
