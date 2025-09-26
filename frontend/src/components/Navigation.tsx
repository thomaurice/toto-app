import { useLocalStorage } from "@uidotdev/usehooks";
import { Link } from "react-router-dom";
import { useApi } from "../api/useApi";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { Button } from "../design-system/Button";

export default function Navigation() {
  const [token, setToken] = useLocalStorage("token", "");
  const queryClient = useQueryClient();
  const handleLogout = () => {
    setToken("");
    queryClient.clear();
  };
  const api = useApi();
  const { data } = useQuery({
    queryKey: ["currentUser"],
    queryFn: api.getCurrentUser,
    enabled: !!token,
  });
  const currentUser = data?.data;

  return (
    <div>
      {currentUser && (
        <div>
          <span>Logged in as: {currentUser.username}</span>
          <Button onClick={handleLogout}>Logout</Button>
        </div>
      )}

      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        {!currentUser && <Link to="/login">Login</Link>}
        {!currentUser && <Link to="/register">Register</Link>}
      </nav>
    </div>
  );
}
