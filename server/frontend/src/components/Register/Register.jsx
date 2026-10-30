import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const gohome = () => {
    window.location.href = window.location.origin;
  };

  const register = async (e) => {
    e.preventDefault();

    let register_url = window.location.origin + "/djangoapp/register";

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email,
      }),
    });

    const json = await res.json();
    if (json.status) {
      sessionStorage.setItem("username", json.userName);
      window.location.href = window.location.origin;
    } else if (json.error === "Already Registered") {
      alert("The user with same username is already registered");
      window.location.href = window.location.origin;
    }
  };

  return (
    <div className="register_container" style={{ width: "50%", margin: "auto", marginTop: "5%" }}>
      <div className="header" style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}>
        <span className="text" style={{ flexGrow: "1", fontSize: "28px", fontWeight: "bold" }}>Sign Up</span>
        <div style={{ display: "flex", flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
          <a href="/" onClick={() => gohome()} style={{ cursor: "pointer", textDecoration: "none", fontSize: "20px" }}>
            ✕
          </a>
        </div>
        <hr />
      </div>

      <form onSubmit={register}>
        <div className="inputs" style={{ display: "flex", flexDirection: "column", gap: "14px", marginTop: "20px" }}>
          {/* Input 1: Username */}
          <div className="input">
            <input
              type="text"
              name="username"
              placeholder="Username"
              className="input_field"
              required
              onChange={(e) => setUserName(e.target.value)}
            />
          </div>

          {/* Input 2: First Name */}
          <div className="input">
            <input
              type="text"
              name="firstName"
              placeholder="First Name"
              className="input_field"
              required
              onChange={(e) => setFirstName(e.target.value)}
            />
          </div>

          {/* Input 3: Last Name */}
          <div className="input">
            <input
              type="text"
              name="lastName"
              placeholder="Last Name"
              className="input_field"
              required
              onChange={(e) => setLastName(e.target.value)}
            />
          </div>

          {/* Input 4: Email */}
          <div className="input">
            <input
              type="email"
              name="email"
              placeholder="Email"
              className="input_field"
              required
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          {/* Input 5: Password */}
          <div className="input">
            <input
              name="password"
              type="password"
              placeholder="Password"
              className="input_field"
              required
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
        </div>

        {/* Submit Button */}
        <div className="submit_panel" style={{ marginTop: "20px" }}>
          <input className="submit btn btn-primary w-100" type="submit" value="Register" />
        </div>
      </form>
    </div>
  );
};

export default Register;
