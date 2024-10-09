import style from "./index.module.css";

function Name({ designation, name, setName }) {
  return (
    <div className={style.Name}>
      <h1>{designation}</h1>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Write filter name"
      ></input>
    </div>
  );
}

export default Name;
