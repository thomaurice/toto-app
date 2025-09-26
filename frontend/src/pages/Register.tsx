import { useCallback, useState } from "react";
import { useMutation } from "@tanstack/react-query";

import type { UserCreate } from "../api";
import { useLocalStorage } from "@uidotdev/usehooks";
import { useApi } from "../api/useApi";
import { useNavigate } from "react-router-dom";
import { Button } from "../design-system/Button";
import { Field, Fieldset, Input, Label } from "@headlessui/react";

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

  const handleSubmit = useCallback(() => {
    registerMutation.mutate(formData);
  }, [formData, registerMutation]);

  const changeUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({
      ...prev,
      username: e.target.value,
    }));
  };

  const changePassword = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({
      ...prev,
      password: e.target.value,
    }));
  };

  return (
    <>
      <title>Register</title>

      <h1>Register</h1>
      <Fieldset>
        <Field>
          <Label>Username:</Label>
          <Input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={changeUsername}
            required
          />
        </Field>

        <Field>
          <Label>Password:</Label>
          <Input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={changePassword}
            required
          />
        </Field>
      </Fieldset>
      <Button onClick={handleSubmit} disabled={registerMutation.isPending}>
        {registerMutation.isPending ? "Creating account..." : "Register"}
      </Button>
      {registerMutation.isError && (
        <div>Registration failed. Please try again.</div>
      )}
    </>
  );
}
