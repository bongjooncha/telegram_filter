import React from "react";
import Main from "pages/main";
import EditGroup from "pages/editGroup";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/edit_group" element={<EditGroup />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
