import style from "./index.module.css";

function Name({ designation, name, setName }) {
  return (
    <div className={style.Name}>
      <h2>{designation}</h2>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="제목 입력"
      ></input>
    </div>
  );
}

export default Name;
