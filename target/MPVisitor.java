// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#mptype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMptype(MPParser.MptypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#body}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBody(MPParser.BodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp(MPParser.ExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#funcall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncall(MPParser.FuncallContext ctx);
}