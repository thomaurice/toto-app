import { Button as HeadlessButton } from "@headlessui/react";

const Button = ({
  children,
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement>) => {
  return (
    <HeadlessButton className={"cursor-pointer"} {...props}>
      {children}
    </HeadlessButton>
  );
};
export { Button };
