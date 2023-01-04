import './css/App.css';
import { RequireToken, setupAxios } from './helpers/Auth'
import CreateUser from "./components/user/create_user";
import Login from './components/login/Login';
import Logout from './components/login/Logout';
import Navbar from "./components/navbar/navbar"
import VerifyUser from './components/user/VerifyUser';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {
  setupAxios();
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/create_user" element={<CreateUser />} />
        <Route path="/logout" element={<RequireToken><Logout /></RequireToken>} />
        <Route path="/verify_user" element={<VerifyUser />} />
      </Routes>
    </Router>
  );
}

export default App;
