import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Card from './Card.jsx'
import FundamentalsCard from './homecards/FundamentalsCard'
import HTMLcard from './homecards/HTMLcard'
import CSScard from './homecards/CSScard'
import JavascriptCard from './homecards/JavascriptCard'
import PythonCard from './homecards/PythonCard'
import Fundamentals from './pages/Fundamentals'

import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
} from "react-router-dom";

 // imported code from reactrouter.com so we can link pages ///
 
const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <div>
        <App/>
      </div>
    ),
  },


  {
    path: "/card",
    element: <Card/>,
  },
  
{
  path: "/fundamentals",
  element:<Fundamentals/>,
},

{
  path: "/html",
  element: <HTMLcard/>
},

{
  path: "/css",
  element: <CSScard/>
},

{
  path: "/javascript",
  element: <JavascriptCard/>
},

{
  path: "/python",
  element: <PythonCard/>
},

]);


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
