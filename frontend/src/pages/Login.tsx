import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { DefaultApiFactory } from "../api";
import type { UserLogin } from "../api";
import { useLocalStorage } from "@uidotdev/usehooks";

const api = DefaultApiFactory(
  {
    isJsonMime: (mime: string) => mime === "application/json",
  },
  "http://localhost:8000"
);

export default function Login() {
  const [formData, setFormData] = useState<UserLogin>({
    username: "",
    password: "",
  });
  const [, setPersistedToken] = useLocalStorage("token", "");

  const loginMutation = useMutation({
    mutationFn: (loginData: UserLogin) => api.loginUser(loginData),
    onSuccess: (response) => {
      setPersistedToken(response.data);
    },
    onError: (error) => {
      console.error("Login failed:", error);
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
          <button type="submit" disabled={loginMutation.isPending}>
            {loginMutation.isPending ? "Logging in..." : "Login"}
          </button>
        </form>
      </div>
    </>
  );
}
