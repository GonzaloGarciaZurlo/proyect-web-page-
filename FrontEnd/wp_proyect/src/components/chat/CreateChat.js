import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import '../../css/forms.css';

function CreateChat() {
  const navigate = useNavigate();

  const [chat, setchat] = useState({
    name: "",
    password: ""
  });

  const [error, setErrors] = useState("");

  const handleInputChange = (event) => {
    setchat({
      ...chat,
      [event.target.name]: event.target.value,
    });
  };

  const onSubmit = (event) => {
    event.preventDefault();
    axios
      .post(`${process.env.REACT_APP_BACKEND_URL}/create_chat`, chat)
      .then(function (response) {
        if (response.data.chat_id) {
          navigate(`/lobby/${response.data.chat_id}`);
        } else if (response.data.error) {
          setErrors(response.data.error);
        }
      })
      .catch(function (error) {
        setErrors(error.message);
      });
  };

  const goHome = () => {
    navigate('/')
  }

  return (
    <div className="container">
      <div className="row justify-content-center pt-5 mt-5 mr-1">
        <div className="col-md-10 box">
          <h2 className="text-center" >Create Chat</h2>
          <hr></hr>
          <div className="row justify-content-center">
            <form className="col-10 mx-5 my-4" onSubmit={onSubmit}>
              <label className="form-label">Name: </label>
              <input className="form-control my-form-control"
                data-testid="name-input"
                type="text"
                name="name"
                onChange={handleInputChange}
                required
              />
            <label className="form-label">Password: </label>
              <input className="form-control my-form-control"
                data-testid="name-input"
                type="text"
                name="password"
                onChange={handleInputChange}
                option
              />
              
              <button type="button" className="my-btn" onClick={goHome} >Go Home</button>
              <button className="my-btn" type="submit">Create chat</button>
              {error && <div>{error}</div>}
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CreateChat;
