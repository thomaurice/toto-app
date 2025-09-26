import { useLocalStorage } from "@uidotdev/usehooks";
import { Link } from "react-router-dom";

export default function Navigation() {
  const [token, setToken] = useLocalStorage("token", "");
  const handleLogout = () => {
    setToken("");
  };

  return (
    <div>
      {token && (
        <div>
          <span>Logged in as: {token}</span>
          <button onClick={handleLogout}>Logout</button>
        </div>
      )}

      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/login">Login</Link>
      </nav>
    </div>
  );
}
