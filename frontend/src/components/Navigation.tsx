import { Link } from "react-router-dom";

export default function Navigation() {
  const handleLogout = () => {
    localStorage.removeItem("token");
  };
  const token = localStorage.getItem("token");

  return (
    <div>
      <div>
        <span>Logged in as: {token}</span>
        <button onClick={handleLogout}>Logout</button>
      </div>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/login">Login</Link>
      </nav>
    </div>
  );
}
