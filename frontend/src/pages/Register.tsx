import { useState } from "react";
import { useMutation } from "@tanstack/react-query";

import type { UserCreate } from "../api";
import { useLocalStorage } from "@uidotdev/usehooks";
import { useApi } from "../api/useApi";
import { useNavigate } from "react-router-dom";
import { Button } from "../design-system/Button";

export default function Register() {
  const [formData, setFormData] = useState<UserCreate>({
    username: "",
    password: "",
  });
  const [, setPersistedToken] = useLocalStorage("token", "");
  const api = useApi();
  const navigate = useNavigate();
  const registerMutation = useMutation({
    mutationFn: (registerData: UserCreate) => api.registerUser(registerData),
    onSuccess: (response) => {
      setPersistedToken(response.data);
      navigate("/");
    },
    onError: (error) => {
      console.error("Registration failed:", error);
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    registerMutation.mutate(formData);
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
      <title>Register</title>
      <div>
        <h1>Register</h1>
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
          <Button type="submit" disabled={registerMutation.isPending}>
            {registerMutation.isPending ? "Creating account..." : "Register"}
          </Button>
        </form>
        {registerMutation.isError && (
          <div>Registration failed. Please try again.</div>
        )}
      </div>
    </>
  );
}
