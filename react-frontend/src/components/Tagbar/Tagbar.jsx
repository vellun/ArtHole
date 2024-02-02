import { useState, React } from "react";
import TagButton from "./TagButton";
import "./Tagbar.css";

function Tagbar() {
  const tags = [
    "Все работы",
    "Подписки",
    "Фан арт",
    "Иллюстрация",
    "Концепт-арт",
    "Аниме/манга",
    "Пейзаж",
    "Архитектура",
    "Комикс",
    "Портрет",
  ];

  const [currentTag, setCurrentTag] = useState(tags[0]);

  function handleClick(tagName) {
    console.log(tagName);
    setCurrentTag(tagName);
  }

  return (
    <div className="tags">
      <ul className="tags_ul">
        {tags.map((tag, index) => (
          <li className={currentTag === tag ? "tag-li-active" : "tag-li"}>
            <TagButton
              isActive={currentTag === tag}
              onClick={() => handleClick(tag)}
              key={index}
            >
              {tag}
            </TagButton>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Tagbar;
