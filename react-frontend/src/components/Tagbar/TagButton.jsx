import {React, useState} from "react";
import "./Tagbar.css";

function TagButton({ children, isActive, onClick }) {
  return <a onClick={onClick} className={isActive ? "tag-button-active" : "tag-button"} href="#">
    {children}
  </a>;
}

export default TagButton;
