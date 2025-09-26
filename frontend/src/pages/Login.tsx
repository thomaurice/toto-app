import { useState } from "react";
import { useMutation } from "@tanstack/react-query";

import type { UserLogin } from "../api";
import { useLocalStorage } from "@uidotdev/usehooks";
import { useApi } from "../api/useApi";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [formData, setFormData] = useState<UserLogin>({
    username: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [, setPersistedToken] = useLocalStorage("token", "");
  const api = useApi();
  const navigate = useNavigate();
  const loginMutation = useMutation({
    mutationFn: (loginData: UserLogin) => api.loginUser(loginData),
    onSuccess: (response) => {
      setPersistedToken(response.data);
      navigate("/");
    },
    onError: () => {
      setErrorMessage("Invalid username or password");
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    loginMutation.mutate(formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <>
      <title>Login</title>
      <div>
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          {errorMessage && <p>{errorMessage}</p>}
          <button type="submit" disabled={loginMutation.isPending}>
            {loginMutation.isPending ? "Logging in..." : "Login"}
          </button>
        </form>
      </div>
    </>
  );
}
