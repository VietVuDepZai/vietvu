import { Route, BrowserRouter as Router, Routes } from "react-router-dom";

import  Footer from "./components/Footer.jsx";
import  Navbar from "./components/Navbar.jsx";

import { About, Contact, Home, Projects, Game } from "./pages/index.js";

const App = () => {
  return (
    <main className='bg-slate-300/20'>
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route
            path='/*'
            element={
              <>
                <Routes>
                  <Route path='/about' element={<About />} />
                  <Route path='/projects' element={<Projects />} />
                  <Route path='/contact' element={<Contact />} />
                  <Route path='/2048' element={<Game />} />
                </Routes>
                <Footer />
              </>
            }
          />
        </Routes>
      </Router>
    </main>
  );
};

export default App;
